# 🧠 Django Encyclopedia Wiki

A simple but feature-rich Wikipedia-style encyclopedia built with Django. Users can view, search, create, edit, and explore entries written in Markdown.

## 🔧 Features

### 📄 Entry Page
- Access an encyclopedia entry via `/wiki/TITLE`.
- Renders Markdown content as HTML on the entry page.

### 📚 Index Page
- Home page (`/`) displays a list of all encyclopedia entries.
- Entries are clickable links that navigate to the corresponding entry page.

### 🔍 Search
- Search bar in the sidebar allows users to search for entries.
- If the search query matches a title exactly, the user is redirected to that entry.
- If the search query is a substring match, a results page displays all matching entries.

### 📝 Create New Page
- "Create New Page" in the sidebar leads to a form.
- Users can specify a title and input Markdown content.
- Upon submission, the page is saved and accessible via `/wiki/TITLE`.

### ✏️ Edit Page
- Each entry page includes an "Edit" link.
- The edit form is pre-filled with the current Markdown content.
- Users can modify and save the content.

### 🎲 Random Page
- "Random Page" link in the sidebar takes the user to a random entry.

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-wiki.git
   cd django-wiki
