using System.Windows;
using static bazPlannerWPF.Owner;
using static bazPlannerWPF.Project;

namespace bazPlannerWPF
{
    public partial class auth : Window
    {
        public auth()
        {
            InitializeComponent();
        }

        private void AuthToDB(object sender, RoutedEventArgs e)
        {
            ((MainWindow)Application.Current.MainWindow).labelAuth.Content =  Auth(TextBoxUser.Text, TextBoxPassword.Text);
            SelectProject(Auth(TextBoxUser.Text, TextBoxPassword.Text));
            //((MainWindow)Application.Current.MainWindow).listElements.Items.Add(SelectProject());
            Close();
        }
    }
}