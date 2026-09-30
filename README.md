# Racehorse Conditioning Science

競走馬の解剖・運動生理・傷害・評価・介入を科学的根拠と限界から学ぶ教育サイト。

- 公開URL: https://racehorse.hiluco.net
- Workers URL: https://racehorse-conditioning.hiluco.workers.dev
- Cloudflare account: HILUCO
- Astro + TypeScript / MDX / Zod / Pagefind / Workers Static Assets

## 開発

Node.js 24推奨。Astro checkの対応に合わせTypeScript 6を使用。

```sh
npm ci
npm run dev
npm run typecheck
npm run test
npm run build
npm run preview
```

プレビューが表示する実際のポートを利用してください。別プロセスがポートを使用していると変更されます。

## デプロイ

```sh
npm run deploy
```

`wrangler.jsonc`にHILUCOのaccount_idと専用サブドメインを明示。新しい本番ドメインへ変更する場合は`astro.config.mjs`のsiteも変更します。

## CI と Workers Builds

GitHub Actionsでmain push / PR時に型検査、コンテンツ整合性テスト、ビルドを実行します。

Workers Buildsの接続設定（初回にCloudflareで認証が必要）:

- Repository: yuto-tashiro/racehorse-conditioning
- Worker: racehorse-conditioning
- Production branch: main
- Root directory: /
- Build command: `npm run typecheck && npm run test && npm run build`
- Deploy command: `npx wrangler deploy`
- Non-production branch deploy command: `npx wrangler versions upload`
- Non-production branch builds: enabled
- Node: 24

初回公開時、CLIのOAuthではWorkers Builds Configuration権限がなくAPIが403を返しました。公開自体は完了していますが、Workers Builds接続はダッシュボードのSettings > Buildsから行う必要があります。接続後はmain pushで本番、他ブランチでpreviewが作成されます。

## コンテンツ構造

- `src/content/articles/*.mdx`: 36記事。本文とEvidence claim、対象種、レビュー日、関連リンク。
- `src/content/evidence/*.json`: 検証済み書誌と研究の対象・方法・限界。
- `src/lib/evidence.ts`: Zodスキーマ、独立したLevel / Effect、更新警告。
- `src/pages/articles/[id].astro`: 医学記事の共通表示と関連情報。

記事のreferencesとclaim.referencesはEvidenceのIDを参照。relatedは記事IDを参照します。テストで参照切れと必須項目を検出します。未確認のサンプル数はnullにし、推測で埋めません。

医学記事は文献確認済み・獣医師監修前です。文献の確認範囲（抄録／全文／機関資料）を表示します。Levelは正式なGRADE評価ではなく、掲載文献の範囲に基づく暫定的な編集判断です。専門家によるレビューと内容拡充を継続してください。

## ブラウザ検証

Google Chromeがある環境でプレビューを起動した後:

```sh
TEST_URL=http://127.0.0.1:4321 node scripts/verify-site.mjs
```

日本語・英語検索、空状態、文献フィルター、メニュー、症例解説、内部リンク、モバイル横はみ出し、axeのWCAG A/AAを検証します。`QA_DIR`で結果の保存先を変更できます。

## 今後の範囲

Phase 2のTraining Load simulator、Phase 3の仮想データDashboard、Phase 4の外部論文自動取り込み・Knowledge Graph、将来的なAsk the Evidenceは未実装です。診断AIや個体への処方機能はありません。
