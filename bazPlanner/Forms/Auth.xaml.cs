using System.Windows;
using bazPlanner.Models;
using System.Diagnostics;

namespace bazPlanner.Forms
{
    public partial class Auth : Window
    {
        public Auth()
        {
            InitializeComponent();
        }

        //Test connect to database and view projects.
        private void ClickForAuth(object sender, RoutedEventArgs e)
        {
            if (Database.SelectOwner(textOwnerName.Text, textOwnerPass.Password.ToString()) == 1)
            {
                Debug.WriteLine("Success!");
                ((MainWindow)Application.Current.MainWindow).labelAuth.Content = textOwnerName.Text;
                Database.SelectProjects(textOwnerName.Text);
                ((MainWindow)Application.Current.MainWindow).buttonAddProject.IsEnabled = true;
                ((MainWindow)Application.Current.MainWindow).buttonAddTask.IsEnabled = true;
                ((MainWindow)Application.Current.MainWindow).buttonUpdateTask.IsEnabled = true;
                ((MainWindow)Application.Current.MainWindow).buttonDeleteTask.IsEnabled = true;
            }
            else
            {
                Debug.WriteLine("Abort!");
            }           
            Close();
        }
    }
}
