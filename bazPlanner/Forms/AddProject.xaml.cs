using System.Windows;
using bazPlanner.Models;

namespace bazPlanner.Forms
{
    /// <summary>
    /// Логика взаимодействия для AddProject.xaml
    /// </summary>
    public partial class AddProject : Window
    {
        public AddProject()
        {
            InitializeComponent();
        }

        private void CreateNewProject(object sender, RoutedEventArgs e)
        {
            Database.InsertProject("test", "admin");
        }
    }
}
