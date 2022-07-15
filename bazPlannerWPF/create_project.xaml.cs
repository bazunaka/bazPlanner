using System.Windows;
using static bazPlannerWPF.Project;

namespace bazPlannerWPF
{
    public partial class Create_project : Window
    {
        public Create_project()
        {
            InitializeComponent();
        }

        private void AddProject(object sender, RoutedEventArgs e)
        {
            InsertProject(textNameProject.Text, ((MainWindow)Application.Current.MainWindow).labelAuth.Content.ToString());
        }
    }
}
